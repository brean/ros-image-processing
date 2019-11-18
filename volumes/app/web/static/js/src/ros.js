/* ROS Service communication */
class ROS extends ROSLIB.Ros {
  constructor() {
    super();
    this.on('connection', this.onConnected.bind(this));
    this.on('error', this.onError.bind(this));
    this.on('close', this.onClose.bind(this));
    let location = window.location.toString();
    let proto = window.location.protocol === 'http:' ? 'ws:' : 'wss:';
    this.connect(`${proto}//${window.location.hostname}:9090`, {
      protocolVersion: 8,
      origin: location,
      rejectUnauthorized: false
    });
  }

  onConnected() {
    console.log('Connected to websocket server.');
  }

  onError(error) {
    console.log('Error connecting to websocket server: ', error);
  }

  onClose() {
    console.log('Connection to websocket server closed.');
  }

}

const ros = new ROS();
