# Honeybee Anvil Prototype

## Prerequisites

* Python 2.7 (`apt-get install python2.7` or [https://www.python.org/downloads/](https://www.python.org/downloads/))
* pip 9.01 (installed with python, check with `pip --version`, upgrade with `pip install --upgrade pip`)
* pipenv (`pip install pipenv`)

## Building and running

1. Install Python dependencies and activate the environment

   ```
   $ pipenv install
   $ pipenv shell
   ```

2. Compile proto files into message and service Python classes

   ```
   $ python -m grpc.tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/honeybee.proto
   $ python -m grpc.tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/anvilCore/*.proto
   ```

3. Run the server

   ```
   $ python server.py
   Starting Honeybee on [::]:50001
   ```

4. Test with grpcc (in another shell window)

   ```
   $ npm install -g grpcc
   $ grpcc --proto ./proto/honeybee.proto --address 127.0.0.1:50001 -i
   RunRecipe@127.0.0.1:50001> client.run({"id": 0, "hoys": [10, 11, 12], "location": { "city": "-", "latitude": 40.7128, "longitude": 74.0060, "time_zone": 5, "elevation": 33}, "analysis_grids": {"analysis_points": [{"direction": {"x": 0, "y": 0, "z": 1}, "location": {"x": 0, "y": 0, "z": 0}}]}}, pr)
   EventEmitter{}
   RunRecipe@127.0.0.1:50001>
   {
     "job_id": "random_id",
     "success": true,
     "values": [
        {
          "hoy": 12,
          "total": 1,
          "direct": 0
        },
        {
          "hoy": 13,
          "total": 1,
          "direct": 0
        },
        {
          "hoy": 14,
          "total": 1,
          "direct": 0
        }                
     ],
     "log_info": "TODO: Add logging!"
   }
   RunRecipe@127.0.0.1:50001>
   ```

## Notes

* On Windows, you may need to prefix any python commands with `winpty` in order to see console output, for example:
   ```
   $ winpty python server.py
   ```
