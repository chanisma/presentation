## Handoff: team-plan → team-exec (Cycle 3 - Image Search Improvement)

### Pipeline: Presentation Builder Image Search Improvement

**Task**: Improve the presentation-builder skill's Playwright-based image search and integration functionality through scenario-driven testing and validation.

**Pipeline Structure** (Sequential):
1. **worker-1**: Scenario generation (3 diverse presentation scenarios with image search focus)
2. **worker-2**: Image search & download via Playwright (blocked by #1)
3. **worker-3**: HTML presentation creation (blocked by #1, #2)
4. **worker-4**: Playwright validation of image rendering (blocked by #3)
5. **worker-5**: Skill improvement based on findings (blocked by #4)

**Key Files**:
- Skill: `E:\presentation\.claude\SKILL.md`
- Image search ref: `E:\presentation\.claude\references\web-image-search.md`
- HTML template ref: `E:\presentation\.claude\references\html-template.md`
- Styles ref: `E:\presentation\.claude\references\styles.md`
- Test pages.json: `E:\presentation\test\pages.json`

**Decided**:
- Output folders: `test/cycle3-1-*`, `test/cycle3-2-*`, `test/cycle3-3-*`
- Naming convention follows existing cycle2-* pattern
- Presentations must NOT be deleted after creation
- All intermediate artifacts (scenarios.md, scenarios.json, reports) stay in test/

**Risks**:
- Google may block automated image searches (CAPTCHA)
- Playwright MCP connection may be unstable
- Image downloads may fail due to CORS/hotlinking restrictions

**Remaining**: Execute pipeline stages sequentially, main lead monitors and summarizes.
