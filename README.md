# ttp-notify
Trusted Traveler Programs (TTPs) such as Global Entry are great, but trying to find available appointments is almost impossible at some locations. This tool will watch for open appointments at desried locations and notify when one is available.

For information on TTPs, see: https://ttp.cbp.dhs.gov/

This project was inspired by: https://github.com/Drewster727/goes-notify

## Location IDs
For Global Entry: https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=Global%20Entry

## Notification Methods
Currently the only notification method is a webhook trigger on IFTTT. In the request, `value1` is set to the enrollment center location and `value2` is set to the date/time of the available appointment.

## Docker
I use Docker Compose to manage execution. While Docker is not required, the environmental variable are. Below is a sample Docker Compose file:
```yaml
version: "3.8"
services:
  notify:
    build: .
    environment:
      IFTTT_WEBHOOK_URL: https://maker.ifttt.com/foo/bar
      LOCATION_IDS: 1001,1002,1003
    restart: unless-stopped
```
