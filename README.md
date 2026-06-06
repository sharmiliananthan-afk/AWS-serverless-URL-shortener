Serverless URL Shortener — AWS

![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Serverless](https://img.shields.io/badge/Architecture-Serverless-blue)
![Free Tier](https://img.shields.io/badge/Cost-Free%20Tier-green)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

A production-grade serverless URL shortening service built 
on AWS — similar to bit.ly but built from scratch!

Live Demo
👉 https://your-cloudfront-url.cloudfront.net

## 🏗 Architecture
User → CloudFront → S3 (Frontend)
↓
API Gateway
↓         ↓
POST /shorten  GET /{code}
↓         ↓
Lambda Create  Lambda Redirect
↓         ↓
DynamoDB ←───┘

## ✨ Features
- Shorten any URL instantly
- Automatic redirect to original URL
- Serverless — no servers to manage
- Globally distributed via CloudFront CDN
- Error handling for invalid URLs

## 🛠 AWS Services Used
| Service | Purpose |
|---|---|
| S3 | Hosts frontend HTML |
| CloudFront | CDN + HTTPS delivery |
| API Gateway | REST API endpoints |
| Lambda (Python) x2 | Create + Redirect functions |
| DynamoDB | Stores URL mappings |
| IAM | Security and permissions |

## 📁 Project Structure
aws-serverless-url-shortener/
├── index.html          # Frontend UI
├── lambda_create.py    # POST /shorten Lambda
├── lambda_redirect.py  # GET /{shortCode} Lambda
└── README.md

## 🔌 API Endpoints
POST /shorten
Body: {"url": "https://long-url.com"}
Returns: {"shortCode": "abc123"}
GET /{shortCode}
Returns: 301 redirect to original URL

## 💰 Cost
~$0/month on AWS Free Tier

## 📚 What I Learned
- Serverless architecture design
- REST API development with API Gateway
- NoSQL data storage with DynamoDB
- CORS configuration
- Lambda function chaining
- CloudFront CDN setup
