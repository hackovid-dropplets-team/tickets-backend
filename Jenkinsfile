node {
    stage('Build image') {
        def image = docker.image 'hackovid-dropplets-team/tickets-backend' 'tickets-backend'
    }
    stage('Publish image') {
        image.push 'latest'
    }
}