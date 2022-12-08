## About the project:
We get this project as home task at "Method for Detection of Cyber Attacks" course.
The input we get is csv file that contain network data from a phisical hosts.

### Data fields in the csv file:
● record ID - The unique identifier for each connection record.
● Duration_- This feature denotes the number of seconds (rounded) of the connection. For 
example, a connection for 0.17s or 0.3s would be indicated with a “0” in this field.
● src_bytes This field represents the number of data bytes transferred from the source to the 
destination (i.e., the number of outgoing bytes from the host).
● dst_bytes This feature represents the number of data bytes transferred from the destination 
to the source (i.e., the number of bytes received by the host).

## How to run the docker:
In order to run the application with the docker properly you need the follow the next orders

Change directory to the app directory. Replace \path\to\app with the path to your getting-started\app directory:

```bash
cd \path\to\app
```

For building the docker:

```bash
docker build -t getting-started .
```

For running the docker:

```bash
docker run -dp 5000:5000 getting-started
```

Than, open your browser and write in the URL for presention the application UI:

```bash
"localhost:5000"
```
