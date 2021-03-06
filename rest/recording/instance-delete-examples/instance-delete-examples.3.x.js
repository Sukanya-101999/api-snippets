// Download the Node helper library from twilio.com/docs/node/install
// These consts are your accountSid and authToken from https://www.twilio.com/console
const accountSid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';
const authToken = 'your_auth_token';
const client = require('twilio')(accountSid, authToken);

const recordingSid = 'RE557ce644e5ab84fa21cc21112e22c485';

client
  .recordings(recordingSid)
  .remove()
  .then(() => console.log(`Sid ${recordingSid} deleted successfully.`))
  .catch(err => {
    console.log(err.status);
    throw err;
  });
