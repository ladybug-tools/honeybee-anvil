import honeybee_pb2
import honeybee_pb2_grpc

from protobuf_to_dict import protobuf_to_dict
from honeybee_job import run_from_json
import uuid


class HoneybeeService(honeybee_pb2_grpc.RunRecipeServicer):

    def run(self, request, context):
        # convert request to json
        job_id = str(uuid.uuid4())
        recipe = protobuf_to_dict(request)
        if 'id' not in recipe:
            recipe['id'] = 0
        if 'location' not in recipe:
            recipe['location'] = {}
        if 'surfaces' not in recipe:
            recipe['surfaces'] = []

        # map x, y, z to tuple
        # This is a hack. I need to fix the JSON schema for honeybee to handle this case
        for ag in recipe['analysis_grids']:
            for ap in ag['analysis_points']:
                dirc = ap['direction']
                loc = ap['location']
                new_dir = []
                new_loc = []
                for v in ('x', 'y', 'z'):
                    if v in dirc:
                        new_dir.append(dirc[v])
                    else:
                        new_dir.append(0)
                    if v in loc:
                        new_loc.append(loc[v])
                    else:
                        new_loc.append(0)
                ap['direction'] = new_dir
                ap['location'] = new_loc

        folder = '.'

        success, results = run_from_json(recipe, folder, name=job_id)

        values = []
        if success:
            for ag in results:
                for ap in ag['analysis_points']:
                    for value in ap['values'][0]:
                        for k, v in value.iteritems():
                            values.append({'hoy': k, 'total': v[0], 'direct': v[1]})

        # map results to radiance results
        return honeybee_pb2.Result(
            job_id=job_id,
            success=success,
            values=values,
            log_info='TODO: Add logging!'
        )

    @classmethod
    def add_to_server(cls, server):
        honeybee_pb2_grpc.add_RunRecipeServicer_to_server(HoneybeeService(), server)
