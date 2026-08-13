import httpx
from fastapi import Request, HTTPException

async def forward_request(url: str, request: Request):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=request.method,
                url=url,
                content=await request.body(),
                headers={"Content-Type": "application/json"}
            )
            return response.json()
        except httpx.ConnectError:
            raise HTTPException(status_code=503, detail="Servis ishlamayapti!")