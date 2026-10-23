# AWS Project Security Checklist

## Network Security
- [ ] Allow HTTP traffic on port 80 only when required.
- [ ] Restrict SSH access on port 22 to my own IP address.
- [ ] Avoid opening unnecessary ports.
- [ ] Do not create a NAT Gateway for this Free Tier-focused project.

## Identity and Access Management (IAM)
- [ ] Use least-privilege permissions.
- [ ] Avoid sharing AWS credentials.
- [ ] Do not upload access keys, passwords, or secrets to GitHub.
- [ ] Use an IAM role for EC2 access to S3 where appropriate.

## S3 Security
- [ ] Keep the S3 bucket private.
- [ ] Enable Block Public Access.
- [ ] Upload only non-sensitive sample data.

## Monitoring and Cost Control
- [ ] Configure a budget and billing alerts.
- [ ] Review running resources regularly.
- [ ] Stop or delete resources when they are no longer needed.
- [ ] Verify costs before creating resources.

## Verification Status
These items are planned checks. Mark each item complete only after verifying the corresponding AWS configuration.

AWS infrastructure has not yet been deployed.
