/**
  * Initializes JFrog CLI with the necessary configuration for the current build.
  */
void initJFrogCLI() {
  withCredentials([usernamePassword(
    credentialsId: 'jfrog-platform-credentials',
    usernameVariable: 'USER',
    passwordVariable: 'TOKEN'
    )]) {
    sh 'jf config add --user $USER --password $TOKEN --url ' + env.JFROG_PLATFORM_URL
    }
  sh "jf pip-config --repo-resolve pypi --repo-deploy ${env.PYPI_DEPLOY_REPO}"
  String[] projectPathParts = env.JOB_NAME.split('/')
  String jobName = URLDecoder.decode(projectPathParts[-2], 'utf-8')
  String branchName = URLDecoder.decode(env.BRANCH_NAME, 'utf-8')
  env.JFROG_CLI_BUILD_NAME = jobName
  env.JFROG_CLI_BUILD_NUMBER = "${branchName}/${env.BUILD_NUMBER}"
  env.JFROG_CLI_BUILD_URL = env.BUILD_URL
  env.JFROG_CLI_REPORT_USAGE = false
  env.JFROG_CLI_FAIL_NO_OP = true
}

/**
  * Publishes the build info to Artifactory and adds a summary and badge to the Jenkins build page.
  */
void publishBuildInfo() {
  Map<String, String> result = readJSON(text: sh(script: 'jf rt build-publish', returnStdout: true).trim())

  String icon = 'symbol-cube plugin-ionicons-api'
  String style = 'color: green'
  String text = 'Artifactory Build Info'
  String link = result['buildInfoUiUrl']

  addSummary(icon: icon, style: style, text: text, link: link, target: '_blank')
  addBadge(icon: icon, style: style, text: text, link: link, target: '_blank')
}

/**
  * Install all package dependencies so that they are linked in the build info JSON.
  */
void populateBuildInfo() {
  // We need to use pip here because JFrog CLI doesn't support astral's uv yet
  // More information: https://github.com/jfrog/jfrog-cli-artifactory/issues/212
  sh 'python3 -m venv venvDependencies'
  sh '''\
    . venvDependencies/bin/activate && \
    jf pip install \
    --module=voraus-example-application \
    --no-cache-dir \
    --force-reinstall \
    .
  '''
}

void publishGitHubRelease() {
  withCredentials([usernamePassword(
    credentialsId: 'github-app',
    usernameVariable: 'GITHUB_APP',
    passwordVariable: 'GITHUB_ACCESS_TOKEN'
    )]) {
    withEnv([
      "JRELEASER_PROJECT_NAME=${env.PACKAGE_NAME}",
      "JRELEASER_PROJECT_VERSION=${env.TAG_NAME}",
      "JRELEASER_GITHUB_TOKEN=${env.GITHUB_ACCESS_TOKEN}".toString(),
      'JRELEASER_SKIP_TAG=true'
    ]) {
      sh 'jreleaser release'
    }
  }
}

return this
