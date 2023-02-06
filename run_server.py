import uvicorn


if __name__ == "__main__":
    app_name = "apps.site.app:app"
    uvicorn.run(
        app_name,
        host="0.0.0.0",
        port=9090, 
        reload=True
        )