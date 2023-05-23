from fastapi import APIRouter

from app.api.routes import stash, stash_plot


router = APIRouter()
router.include_router(stash.router, tags=["stash"])
router.include_router(stash_plot.router, tags=["plot"], prefix="/plot")
