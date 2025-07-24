[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask3&demo-title=Flask%203%20%2B%20Vercel&demo-description=Use%20Flask%203%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask3-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)

# Flask + Vercel

This example shows how to use Flask 3 on Vercel with Serverless Functions using the [Python Runtime](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python).

## Demo

https://flask-python-template.vercel.app/

## How it Works

This example uses the Web Server Gateway Interface (WSGI) with Flask to enable handling requests on Vercel with Serverless Functions.

## Running Locally

```bash
npm i -g vercel
vercel dev
```

Your Flask application is now available at `http://localhost:3000`.
Open this URL in a browser and use the provided form to upload your Excel file.

## One-Click Deploy

Deploy the example using [Vercel](https://vercel.com?utm_source=github&utm_medium=readme&utm_campaign=vercel-examples):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask3&demo-title=Flask%203%20%2B%20Vercel&demo-description=Use%20Flask%203%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask3-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)
After deployment, navigate to the root of your new Vercel project to access the
upload form.

## Uploading an Excel File

When visiting the root path of the deployed application you will see a simple
web form that allows you to upload an Excel spreadsheet. Once processed the
page displays metrics and two heatmaps summarizing the demand and coverage for
the generated schedule.

### Prerequisites

The uploaded file must contain a sheet with at least the following columns:

- `Día` – day of the week as an integer (1 = Monday, 7 = Sunday).
- `Suma de Agentes Requeridos Erlang` – hourly demand for that day.

Each day should have 24 rows representing the hourly requirement. Any extra
columns are ignored by the application.

### Metrics and Heatmaps

After uploading a valid Excel file the page shows:

- **Cobertura**: percentage of demand that was successfully covered.
- **Agentes**: total number of agents scheduled.
- **Exceso** and **Déficit**: overstaffing and understaffing hours.
- Two heatmaps illustrating hourly demand and coverage by day.

Use these metrics to evaluate whether the generated schedule meets your
requirements.
