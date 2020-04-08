node {
    def image = ""
    stage('Build image') {
        image = docker.image("hackovid-dropplets-team/tickets-backend", "tickets-backend")
    }
    stage('Publish image') {
        image.push("latest")
    }
}