# Appointment Booking System - n8n Integration Guide

This guide explains how to set up the complete appointment booking system with n8n workflow automation.

## Features

### Core Appointment Management
- ✅ Create, update, reschedule, and cancel appointments
- ✅ Client management with email/phone contact information
- ✅ Multiple appointment types (consultation, meeting, demo, etc.)
- ✅ Status tracking (scheduled, confirmed, completed, cancelled, no-show)
- ✅ Timeline and history tracking

### Daily Automation (8:00 AM)
- ✅ Automatic Excel export of old/completed appointments
- ✅ Email delivery to admin users
- ✅ Google Sheets integration (optional)
- ✅ Summary statistics and metrics

### Email Notifications
- ✅ Appointment confirmation emails
- ✅ Update notifications
- ✅ Reschedule notifications
- ✅ Cancellation notifications
- ✅ 24-hour reminder emails
- ✅ Follow-up emails after completion

### n8n Workflow Automation
- ✅ Webhook-driven appointment events
- ✅ Scheduled daily exports
- ✅ Automated reminder system
- ✅ Slack/Teams notifications
- ✅ Calendar integration

## Installation & Setup

### 1. Flask Application Setup

1. Install required dependencies:
```bash
pip install flask flask-sqlalchemy flask-migrate flask-login flask-mail flask-wtf
pip install pandas openpyxl schedule python-dotenv
```

2. Set environment variables:
```bash
# Application Settings
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=sqlite:///app.db

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=your-email@gmail.com

# n8n Integration
N8N_API_KEY=your-n8n-api-key
WEBHOOK_SECRET=your-webhook-secret
APP_BASE_URL=http://localhost:5000

# Admin Settings
ADMIN_EMAIL=admin@yourcompany.com

# Optional: Google Sheets
GOOGLE_SHEETS_ID=your-spreadsheet-id
GOOGLE_SHEETS_WEBHOOK_URL=your-google-sheets-webhook

# Optional: Slack Integration
SLACK_WEBHOOK_URL=your-slack-webhook-url
```

3. Initialize the database:
```bash
flask db init
flask db migrate -m "Add appointment models"
flask db upgrade
```

### 2. n8n Setup

1. Import the workflow:
   - Copy the content from `n8n_workflows/appointment_automation_workflow.json`
   - Import it into your n8n instance

2. Configure credentials in n8n:

#### HTTP Header Auth (for API calls)
- Name: `API Auth`
- Header Name: `X-API-Key`
- Header Value: `your-n8n-api-key` (same as N8N_API_KEY)

#### SMTP Credentials (for emails)
- Name: `SMTP Credentials`
- Host: `smtp.gmail.com`
- Port: `587`
- Security: `StartTLS`
- Username: `your-email@gmail.com`
- Password: `your-app-password`

3. Set environment variables in n8n:
```bash
APP_BASE_URL=http://localhost:5000
ADMIN_EMAIL=admin@yourcompany.com
MAIL_USERNAME=your-email@gmail.com
GOOGLE_SHEETS_ID=your-spreadsheet-id
GOOGLE_SHEETS_WEBHOOK_URL=your-google-sheets-webhook
SLACK_WEBHOOK_URL=your-slack-webhook-url
```

### 3. Webhook Configuration

The system uses webhooks to trigger n8n workflows for real-time events:

#### Webhook URL
```
http://your-n8n-instance.com/webhook/appointment-webhook
```

#### Webhook Events
The Flask application sends webhooks for:
- `appointment_created`
- `appointment_updated` 
- `appointment_cancelled`
- `appointment_rescheduled`

#### Example Webhook Payload
```json
{
  "action": "appointment_created",
  "appointment": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "title": "Initial Consultation",
    "client_name": "John Doe",
    "client_email": "john@example.com",
    "scheduled_date": "2024-01-15T14:00:00",
    "status": "scheduled",
    "appointment_type": "consultation"
  },
  "timestamp": "2024-01-14T10:30:00Z"
}
```

## API Endpoints

### For n8n Integration

#### Get Old Appointments
```
GET /api/appointments/old
Headers: X-API-Key: your-api-key
```

#### Get Upcoming Appointments  
```
GET /api/appointments/upcoming
Headers: X-API-Key: your-api-key
```

#### Generate Excel Export
```
POST /api/appointments/export/excel
Headers: X-API-Key: your-api-key
Content-Type: application/json
Body: {"appointments": [...]}
```

#### Send Appointment Reminder
```
POST /api/appointments/{appointment_id}/reminder
Headers: X-API-Key: your-api-key
```

#### Get Appointment Statistics
```
GET /api/appointments/stats
Headers: X-API-Key: your-api-key
```

#### Calendar Events
```
GET /api/appointments/calendar?start=2024-01-01&end=2024-01-31
Headers: X-API-Key: your-api-key
```

## Workflow Components

### 1. Daily Export Workflow (8:00 AM)

**Trigger:** Cron schedule at 8:00 AM daily
**Steps:**
1. Get old appointments from API
2. Check if appointments exist
3. Generate Excel export
4. Send email to admin
5. Update Google Sheets (optional)

### 2. Reminder Workflow (Every 6 hours)

**Trigger:** Cron schedule every 6 hours  
**Steps:**
1. Get upcoming appointments
2. Filter appointments needing reminders (24h before)
3. Send reminder emails
4. Update reminder status

### 3. Event-Driven Workflow

**Trigger:** Webhook on appointment events
**Steps:**
1. Receive webhook payload
2. Check action type (created/updated/cancelled/rescheduled)
3. Send appropriate email notification
4. Notify Slack/Teams (optional)

## Google Sheets Integration

To enable Google Sheets integration:

1. Create a Google Sheets API service account
2. Download the credentials JSON file
3. Share your spreadsheet with the service account email
4. Configure the Google Sheets webhook URL in n8n

Example Google Sheets API call:
```javascript
// In n8n HTTP Request node
{
  "action": "append_rows",
  "spreadsheet_id": "your-spreadsheet-id", 
  "sheet_name": "Appointments",
  "data": [
    ["2024-01-15", "John Doe", "Consultation", "Completed"],
    ["2024-01-16", "Jane Smith", "Demo", "Scheduled"]
  ]
}
```

## Customization

### Adding Custom Appointment Types
1. Update `AppointmentType` enum in `models.py`
2. Update form choices in `forms_appointment.py`
3. Update templates to handle new types

### Custom Email Templates
1. Modify email templates in `routes_appointments.py`
2. Add HTML email support
3. Use template variables for personalization

### Additional Automation
1. Add new cron schedules in n8n
2. Create custom API endpoints
3. Integrate with CRM systems
4. Add SMS notifications

## Monitoring & Logs

### Application Logs
```bash
# View appointment automation logs
tail -f logs/appointment_automation.log

# View Flask application logs  
tail -f logs/app.log
```

### n8n Monitoring
- Check workflow execution history
- Monitor webhook delivery status
- Review error logs for failed executions

### Database Monitoring
```sql
-- Check appointment statistics
SELECT status, COUNT(*) FROM appointments GROUP BY status;

-- Recent appointment activity
SELECT * FROM appointment_history ORDER BY created_at DESC LIMIT 10;

-- Email delivery status
SELECT action, COUNT(*) FROM appointment_history 
WHERE action = 'email_sent' 
GROUP BY details;
```

## Troubleshooting

### Common Issues

1. **Emails not sending**
   - Check SMTP credentials
   - Verify firewall settings
   - Check email quota limits

2. **Webhooks not working**
   - Verify webhook URL accessibility
   - Check API key configuration
   - Review n8n webhook logs

3. **Daily export not running**
   - Check cron schedule configuration
   - Verify timezone settings
   - Review automation logs

4. **Database connection issues**
   - Check DATABASE_URL configuration
   - Verify database migrations
   - Review connection pool settings

### Support

For issues and questions:
1. Check application logs
2. Review n8n workflow execution history  
3. Verify environment configuration
4. Test API endpoints manually

## Security Considerations

1. **API Security**
   - Use strong API keys
   - Implement rate limiting
   - Validate webhook signatures

2. **Email Security**
   - Use app-specific passwords
   - Enable 2FA on email accounts
   - Monitor email delivery

3. **Data Protection**
   - Encrypt sensitive data
   - Regular database backups
   - Secure credential storage

This comprehensive setup provides a fully automated appointment booking system with n8n workflow integration, daily exports, and email notifications as requested.