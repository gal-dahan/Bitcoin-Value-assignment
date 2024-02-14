# Bitcoin-Value-assignment

This project sets up a microservices architecture on Azure Kubernetes Service (AKS) to provide real-time bitcoin value information through two services (Service A and Service B).


## Configuration
- Service A generate random bitcoin value (I can use real API, but it is limited to 100 requests per day)
- Service B calculating the average value of the last 10 minutes.

You can see ![Service B](https://i.ibb.co/VBQwpG3/Service-B.png?raw=true "Title")

### Architecture in the image 
![Service B](https://i.ibb.co/XF7v6G1/architecture.jpg?raw=true "Title")
