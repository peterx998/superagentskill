# Public Release Checklist

Run this checklist before making the repository public.

- [ ] Remove secrets
- [ ] Remove private paths
- [ ] Remove local-only absolute paths if unnecessary
- [ ] Confirm license
- [ ] Confirm `SECURITY.md`
- [ ] Confirm examples contain no private customer/project data
- [ ] Confirm catalog files do not expose local-only private plugin cache content
- [ ] Enable GitHub security settings
- [ ] Create first release tag
- [ ] Run `python scripts/validate_repo.py`
- [ ] Rebuild catalog if skill metadata changed
- [ ] Review `README.md` status badge and update from Private Preview when appropriate
