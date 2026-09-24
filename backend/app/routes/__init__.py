from . import (admin, auth, cases, counterfactuals, episodes, explore, media, progress, reference, search)

ROUTERS = [
    auth.router,
    cases.router,
    episodes.router,
    counterfactuals.router,
    explore.router,
    reference.router,
    search.router,
    progress.router,
    media.router,
    admin.router,
]

__all__ = ["ROUTERS"]
