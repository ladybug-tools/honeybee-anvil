// This file represents the script that Jenkins CI/CD pipeline will execute.
// The stages enumerated bellow will be executed in the order they are written (ex. Deployment should come before running BDD or Load tests)
// For more details regarding the implementation of CIUtils functions, see https://git.autodesk.com/Quantum/CILibrary/blob/master/src/com/quantum/CiUtils.groovy

@Library('PSL@master')
@Library('CILibrary@stable') _

import com.quantum.CiUtils

def utils = new CiUtils(steps, env, docker)
utils.setEnvironmentVariables()

def buildImage = "quantumci/cicd-tools"

def buildCmds = {
    sh """
        pip install pipenv
        PIPENV_VENV_IN_PROJECT=1 pipenv install
    """
}

def lintCmd = "PIPENV_VENV_IN_PROJECT=1 pipenv run pylint server.py"

def utTasks = {
    sh """
    PIPENV_VENV_IN_PROJECT=1 pipenv run pytest --junitxml=xunit.xml
    mv xunit.xml ${env.TEST_REPORT_DIR}/UnitTest-xunit.xml
    """
}

try {
    node(env.JENKINS_NODE_CENTOS) {
        try {
            stage("Checkout") {
                utils.cleanCheckoutAndGetAuthorsId(scm, currentBuild)
                utils.buildPreparation()
            }

            stage('Build') {
                // Automatically increments the version - requires package.json
                utils.getNextSemanticVersion(currentBuild)
                // Runs the build command in a nodejs specific build docker container.
                //utils.buildProject(buildCmds, buildImage)
            }

            stage('Security Scan') {
                //utils.securityScan();
            }

            stage("Lint") {
                //utils.buildProject(lintCmd, buildImage)
            }

            stage("UnitTest") {
                // Runs the unit test command.
                //utils.runUnitTest(utTasks)
            }

            stage("Code Analysis") {
                //utils.sonarQubeScan()
            }

            stage("IntegrationTest") {
                //-block
               /* try {
                    utils.runIntegrationTest(itTasks)
                }catch(err) {
                    throw err
                }*/
            }

            if(utils.isMaster || utils.isDeploymentHackBranch) {
                stage("Dockrize") {
                    // Dockerizes using the dockerfile instructions provided in the project.
                    utils.buildAndPushDockerToDockerHub()
                }

                stage("Deploy Anvil") {
                    utils.deployAnvilService()
                }

                stage("BDD") {
                    /*utils.runBDD(bddTasks,
                        [
                            "framework": "drill",
                            "onLocalService": false
                        ]
                    ) */
                }

                stage("LoadTest") {
                     //utils.runLocust()
                 }
            }
            else {
                stage("BDD-Local") {
                    /*utils.runBDD(bddTasks,
                        [
                            "framework": "drill",
                            "onLocalService": true
                        ]
                    )*/
                }
            }

        } catch (err) {
            throw err
        } finally {
            utils.parseTestReportByJenkins()
            utils.cleanUpBuild()
        }
    }
} catch(err) {
    currentBuild.result = "FAILURE"
    env.FAILURE_MESSAGE += err
}

if(utils.isMaster || utils.isDeploymentHackBranch || utils.isPR) {
    stage("Notification") {
        utils.generateAndSendSlackNotification(currentBuild)
    }
}

echo env.FAILURE_MESSAGE
echo utils.testResultMessage
