# Install Docker and learn about a Dockerfile ![](https://www.docker.com/wp-content/uploads/2022/03/horizontal-logo-monochromatic-white.png)
Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. 

This is a simple definition of *docker*. You shoud go along [this official guide](https://docs.docker.com/get-started/overview/) and learn how to install and use its features.

To get familiarized, run a *docker* container from [this *Hello-World* image](https://hub.docker.com/_/hello-world).

___

# Create a dockerfile to serve your API
Now that you understand how docker works and have created a docker container with the *getting-started* example, you can create a and run a docker container for our API.

The *Dockerfile* must be in the same directory of the API as you can see in `src` folder.

If you followed the [official docker guide](https://docs.docker.com/get-started/overview/) at least until *Part 4* of *Get Started* you should know how to build and run your docker.

In order to share it, create a new *docker repository*, tag your image, push it and test it in the [*Play with docker*](https://labs.play-with-docker.com/) browser.