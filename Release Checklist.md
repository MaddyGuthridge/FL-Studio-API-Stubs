
# Release Checklist

* [ ] Check that CI passed

* [ ] Update version number in `pyproject.toml`

* [ ] Update `fl_model/configuration/schema.json:33`,
      `fl_model/configuration/config_typings.py:13` and
      `fl_model/configuration/target_version.py:25` for major versions.

* [ ] Update `LATEST_API_VERSION` from `fl_model/consts.py` for major versions

* [ ] Write release notes and release
