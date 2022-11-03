#!/bin/bash

set -e  # trigger failure on error - do not remove!
set -x  # display command on output

CHGLOG_FILE="${CHGLOG_FILE:-CHANGELOG.md}"

# determine if bumping needed
NEW_TAG_VERSION=$(poetry run semantic-release print-version)
if [ ! -z "${NEW_TAG_VERSION}" ]; then

    # update package version
    poetry version "${NEW_TAG_VERSION}"

    # collect release notes
    REL_NOTES=$(mktemp)
    poetry run semantic-release changelog --unreleased >> "${REL_NOTES}"

    # update changelog
    TMP_CHGLOG=$(mktemp)
    NEW_TAG_NAME="v${NEW_TAG_VERSION}"
    RELEASE_URL="$(gh repo view --json url -q ".url")/releases/tag/${NEW_TAG_NAME}"
    printf "## [${NEW_TAG_NAME}](${RELEASE_URL}) - $(date -Idate)\n\n" >> "${TMP_CHGLOG}"
    cat "${REL_NOTES}" >> "${TMP_CHGLOG}"
    if [ -f "${CHGLOG_FILE}" ]; then
        printf "\n" | cat - "${CHGLOG_FILE}" >> "${TMP_CHGLOG}"
    fi
    mv "${TMP_CHGLOG}" "${CHGLOG_FILE}"

    # push changes
    git config --global user.name 'github-actions[bot]'
    git config --global user.email 'github-actions[bot]@users.noreply.github.com'
    git add pyproject.toml "${CHGLOG_FILE}"
    COMMIT_MSG="chore: bump version to ${NEW_TAG_VERSION} [skip ci]"
    git commit -m "${COMMIT_MSG}"
    git push origin main

    # create GitHub release (incl. Git tag)
    gh release create "${NEW_TAG_NAME}" -F "${REL_NOTES}"
fi
