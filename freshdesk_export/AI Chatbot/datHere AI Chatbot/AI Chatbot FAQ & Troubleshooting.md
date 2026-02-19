---
title: "AI Chatbot FAQ & Troubleshooting"
tags: []
created_at: 2025-09-24T12:01:25Z
updated_at: 2025-09-24T12:01:25Z
---

# AI Chatbot FAQ & Troubleshooting

## Frequently Asked Questions

### General Questions

**Q: What is AI Chatbot and how does it work?** A: AI Chatbot is an AI-powered assistant that understands natural language queries about your CKAN datasets. It searches, analyzes, and visualizes data based on your questions.

**Q: How accurate is the AI?** A: The AI is highly accurate but currently in beta. Always verify critical information independently, especially for important decisions.

**Q: Can I save my conversations?** A: Yes! Use the Export button (?) in the header to download your conversation as a markdown file.

**Q: Is there a limit to how many questions I can ask?** A: This depends on your account type. Most users have generous limits for normal usage.

**Q: Does the AI remember previous questions in a session?** A: Yes, the AI maintains context throughout your conversation. You can reference previous responses.

### Data & Privacy

**Q: Can the AI access my private datasets?** A: The AI can only access datasets you have permission to view in the CKAN portal.

**Q: Is my conversation data stored?** A: Conversations are stored temporarily for your session. Check your organization's data policy for details.

**Q: Can others see my queries?** A: No, your conversations are private to your account.

**Q: What happens to my data when I clear the conversation?** A: Clearing removes the conversation from your current session. Exported conversations remain in your downloads.

### Features & Capabilities

**Q: What types of charts can the AI create?** A: Bar charts, line graphs, pie charts, scatter plots, heatmaps, and more. Just specify what you want!

**Q: Can the AI combine data from multiple datasets?** A: Yes, the AI can analyze and compare data across multiple datasets when relevant.

**Q: What file formats are supported?** A: CSV, JSON, Excel (XLSX/XLS), and other formats supported by your CKAN instance.

**Q: Can I modify the charts after they're created?** A: You can request modifications by asking follow-up questions. For manual editing, download the chart.

**Q: Does the AI work with real-time data?** A: The AI works with the most recent data available in your CKAN instance. Real-time depends on how often datasets are updated.

## Troubleshooting Guide

### Common Issues and Solutions

#### ? "AI Not Understanding My Query"

**Symptoms:**

- Wrong data returned
- Misinterpreted question
- Irrelevant response

**Solutions:**

1. Rephrase using simpler language
2. Break complex questions into parts
3. Use specific dataset names if known
4. Add more context

**Example Fix:**

```
Instead of: "Show the thing from last year" Try: "Show unemployment data from 2023"
```

---

#### ? "No Datasets Found"

**Symptoms:**

- "I couldn't find any relevant datasets"
- Empty results

**Solutions:**

1. Check spelling of technical terms
2. Try alternative keywords
3. Broaden your search terms
4. Verify the data exists in CKAN

**Example Fix:**

```
Instead of: "labour statistics" Try: "employment data" or "job statistics" or "workforce data"
```

---

#### ? "Charts Not Displaying"

**Symptoms:**

- Blank chart area
- "Chart not available" message
- Loading indefinitely

**Solutions:**

1. Refresh the page (F5)
2. Check browser console for errors (F12)
3. Try a simpler chart type
4. Reduce data points (ask for "top 10" instead of all)
5. Clear browser cache

---

#### ? "Slow Response Times"

**Symptoms:**

- Long wait for responses
- Timeout errors
- "Still thinking..." for extended periods

**Solutions:**

1. Simplify your query
2. Request smaller date ranges
3. Ask for specific datasets rather than broad searches
4. Avoid analyzing very large datasets (>100k records)

**Example Fix:**

```
Instead of: "Analyze all historical data" Try: "Analyze data from the last 3 years"
```

---

#### ? "Login Required Message"

**Symptoms:**

- "Please log in to use the AI assistant"
- Session expired warnings

**Solutions:**

1. Click the login button
2. Check if your session expired (re-login)
3. Verify your account has AI access permissions
4. Clear cookies and login again

---

#### ? "Incorrect Calculations or Data"

**Symptoms:**

- Wrong numbers in response
- Calculations don't match source
- Inconsistent results

**Solutions:**

1. Ask the AI to recalculate
2. Request to see the source data
3. Check the thinking process for errors
4. Verify dataset version/date
5. Report persistent issues

---

#### ? "Context Lost Mid-Conversation"

**Symptoms:**

- AI doesn't remember previous questions
- Have to repeat information
- "I don't have that information" for follow-ups

**Solutions:**

1. Reference the specific previous response
2. Summarize context in your question
3. Check if session timed out
4. Avoid very long conversations (export and start fresh)

**Example Fix:**

```
Instead of: "Add population to that" Try: "Add population data to the unemployment chart you just created"
```

## Tips & Tricks

### Getting Better Results

1. **Use Specific Dates**

   - ❌ "recent data"
   - ✅ "data from January 2023 to December 2023"
2. **Name Your Outputs**

   - ❌ "make a chart"
   - ✅ "create a bar chart"
3. **Specify Groupings**

   - ❌ "show by location"
   - ✅ "group by state" or "group by city"
4. **Set Limits**

   - ❌ "show all cities"
   - ✅ "show top 20 cities by population"

### Understanding the Thinking Process

The "Thinking Process" shows:

- **Search queries** used to find data
- **Datasets** examined
- **Analysis steps** performed
- **Decisions** made by the AI

Click to expand and understand how the AI interpreted your question.

### Error Messages Explained

| Error Message | What It Means | What to Do |
| --- | --- | --- |
| "Dataset not found" | The specific dataset doesn't exist | Check dataset name/ID |
| "Insufficient data" | Not enough data for analysis | Broaden your query |
| "Query too complex" | Too many operations requested | Break into smaller queries |
| "Rate limit exceeded" | Too many requests | Wait a few minutes |
| "Invalid date range" | Dates don't make sense | Check date format |

## Still Need Help?

### Quick Checklist

- [ ] Is your query specific enough?
- [ ] Are you logged in?
- [ ] Is the data you want actually available?
- [ ] Have you tried the example queries?
- [ ] Did you check the thinking process?

### Contact Support

If issues persist after trying these solutions:

1. Export your conversation for reference
2. Note the exact error message
3. Contact your CKAN administrator
4. Include browser and version info

### Report a Bug

Help improve AI Chatbot by reporting:

- Consistent errors
- Incorrect calculations
- UI/display issues
- Feature requests

---

*FAQ & Troubleshooting v2.1 - Beta*