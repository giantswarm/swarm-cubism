## Giant Cubism
This sample application demonstrates using the [Giant Swarm APIs](https://docs.giantswarm.io/reference/api) with Python to provide a visualization of instance metrics for applications running on a Giant Swarm account.

There is a blog post on this if you'd like to get to sleep faster.

### Screenshot
Here's a screenshot of the action:

![action](https://raw.githubusercontent.com/giantswarm/swarm-cubism/master/static/img/screenshot.png)

### Prerequisites
You'll need the following installed on your computer to make all this work:

1. [boot2docker](https://github.com/giantswarm/boot2docker#getting-boot2docker-going-on-os-x)
1. [Giant Swarm account](https://giantswarm.io/request-invite/)
1. A couple of apps running in your account.

![meme within a meme](https://github.com/giantswarm/swarm-cubism/blob/master/static/img/meme.jpg)

**"I bought the airline."** - Saito

### Code Checkout
Checkout the repository locally and switch into it:

    git clone https://github.com/giantswarm/swarm-cubism.git
    cd swarm-cubism

### Quick Launch
Running this application locally is really easy:

    make run

If you'd like to do some live development on the code by mirroring the directory on your computer into the `boot2docker` container:

    make dev

### Deploy to Giant Swarm
Deploying is even easier:

    make up


Enjoy!