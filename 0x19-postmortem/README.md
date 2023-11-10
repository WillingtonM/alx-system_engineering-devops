## Web Stack Debugging Project: Postmortem

### Issue Summary
- **Duration of Outage:** The outage started on November 10, 2023, at 2:00 PM GMT and ended at 4:30 PM GMT.
- **Impact:** The main web service was significantly slowed down, impacting approximately 60% of our users. Users experienced delayed responses and timeouts.
- **Root Cause:** An unexpected surge in database queries due to a recently deployed feature.

### Timeline
- **2:00 PM** - Issue detected when response time alarms were triggered.
- **2:10 PM** - Initial assumption was a network bottleneck.
- **2:30 PM** - Investigations revealed normal network traffic but high database load.
- **3:00 PM** - Team B escalated the issue, suspecting a memory leak in the application.
- **3:30 PM** - Misleading path: Focused on server capacity and memory issues.
- **4:00 PM** - Identified the root cause as a surge in database queries linked to a new feature.
- **4:30 PM** - Temporary fix applied by rolling back the recent deployment.

### Root Cause and Resolution
- **Detailed Cause:** The new feature inadvertently caused repetitive and unnecessary database queries, leading to a bottleneck.
- **Resolution:** We rolled back the feature to its previous state, which normalized the database load.

### Corrective and Preventive Measures
- **Improvements:** 
  - Implementing more robust feature testing to catch such issues pre-deployment.
  - Enhancing our monitoring tools to detect abnormal database activity.
- **Specific Tasks:**
  - Task 1: Conduct a thorough review of the new feature's code to identify and fix the query loop.
  - Task 2: Update the deployment checklist to include a specific check for database query optimization.
  - Task 3: Introduce a new monitoring alert for sudden spikes in database queries.
