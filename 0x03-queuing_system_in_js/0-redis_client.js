const redis  = require('redis');
const client  = redis.createClient({
    host: 'localhost',
    port: 6379
});

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function() {
    console.log("Redis client not connected to the server: ERROR_MESSAGE");
});

client.connect();
