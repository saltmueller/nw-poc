var mqtt = require('mqtt')

client = mqtt.createClient(1883, 'localhost');

client.subscribe('linux/metrics');

client.on('message', function (topic, message) {
  console.log(message);
});

// client.end();

