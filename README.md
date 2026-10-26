# SentinelAI API

This folder contains the FastAPI backend. It can run locally with Uvicorn or
deploy as a Vercel Python serverless function.

## Local development

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

The API is available at <http://localhost:8000>, with interactive
documentation at <http://localhost:8000/docs>.

## Deploy to Vercel

Create a Vercel project with this folder as its **Root Directory**, or run the
following commands from `backend`:

```powershell
npm install --global vercel
vercel login
vercel
vercel --prod
```

Vercel uses [`api/index.py`](./api/index.py) as the serverless entry point and
[`vercel.json`](./vercel.json) to route every request to FastAPI.

Configure these environment variables in the Vercel project settings:

| Variable | Required | Example |
| --- | --- | --- |
| `ALLOWED_ORIGINS` | Yes | `https://your-frontend.vercel.app` |
| `MONGODB_URL` | If reports/data use MongoDB | `mongodb+srv://...` |
| `DATABASE_NAME` | If MongoDB is used | `sentinel_ai` |
| `SECRET_KEY` | Recommended | A generated production secret |

Uploaded files are processed in memory and any temporary files are written
under `/tmp`. Vercel storage is ephemeral, so files must not be treated as
persistent application data.
