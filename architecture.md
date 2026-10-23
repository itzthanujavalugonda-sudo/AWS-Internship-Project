
# AWS Project Architecture

```text
IAM User / Administrator
          |
          v
Custom VPC
  |
  +-- Public Subnet + Internet Gateway
          |
          v
  EC2 Linux Web Server
  (Student Portal Website)
          |
          | IAM Instance Role
          v
       S3 Bucket
  (Assets and Archived Logs)

CloudWatch Metrics and Logs
          |
          v
     CloudWatch Alarms
          |
          v
      SNS Email Alerts

EBS Snapshot --> Backup and Recovery
AWS Budgets --> Cost Alerts
```
