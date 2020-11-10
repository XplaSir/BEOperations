## BEOperations

Business Excellence Operations projects

### Steps to get started with git Flow

> Features features are created based on the branch that it was created from for our case its a copy of the develop branch.

---

    git flow feature start webapi

### Create your task as a feature with Module as prefix

    git flow feature start webapi/gisEndPoint

### Work on your task when finish add to develop branch

    git flow feature finish webapi/gisEndPoint

### A team member can publish a feature branch to the remote sever. This is a push to the remote server

    git flow feature publish webapi/gisEndPoint

### A team member can pull a feature branch and work on it on local machine

    git flow feature pull origin webapi/gisEndPoint
