// Download the twilio-csharp library from twilio.com/docs/csharp/install
using System;
using Twilio;
class Example 
{
  static void Main(string[] args) 
  {
    // Find your Account Sid and Auth Token at twilio.com/user/account
    string AccountSid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
    string AuthToken = "{{ auth_token }}";
    string WorkspaceSid = "{{ workspace_sid }}";
    string WorkflowSid = "{{ workflow_sid }}";
    var client = new TaskRouterClient(AccountSid, AuthToken);

    Workflow workflow = client.GetWorkflow(WorkspaceSid, WorkflowSid);
    Console.WriteLine(workflow.FriendlyName);
  }
}