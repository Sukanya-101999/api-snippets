# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioTaskRouterClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "{{ auth_token }}"
workspace_sid = "{{ workspace_sid }}"
taskqueue_sid = "{{ taskqueue_sid }}"

client = TwilioTaskRouterClient(account_sid, auth_token)

taskqueue = client.taskqueues(workspace_sid).update(taskqueue_sid, target_workers='languages HAS "english"')
print taskqueue.target_workers

# alternatively
taskqueue = client.workers(workspace_sid).get(taskqueue_sid)
taskqueue = taskqueue.update(target_workers='languages HAS "english"')
print taskqueue.target_workers