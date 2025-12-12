from urllib.parse import quote


def define_env(env):
    """Define macros and filters for MkDocs."""

    extra = env.variables.get("extra", {})
    contact = extra.get("contact", {})

    def _value(key, fallback=""):
        return contact.get(key) or fallback

    @env.macro
    def contact_faculty():
        return _value("faculty")

    @env.macro
    def contact_email():
        return _value("email")

    @env.macro
    def contact_phone():
        return _value("phone_display")

    @env.macro
    def contact_phone_uri():
        return _value("phone")

    @env.macro
    def contact_website_label():
        return _value("website_label") or _value("website_url")

    @env.macro
    def contact_website_url():
        return _value("website_url")

    @env.macro
    def contact_tagline():
        faculty = contact_faculty()
        website_label = contact_website_label()
        website_url = contact_website_url()
        if not any((faculty, website_url)):
            return ""
        pieces = []
        if faculty:
            pieces.append(f"**{faculty}**")
        if website_url:
            link = f"[{website_label}]({website_url})"
            pieces.append(link)
        return "\n\n".join(pieces)

    def _mailto_link(value, label=None, subject=None):
        if not value:
            return ""
        label = label or value
        href = f"mailto:{value}"
        if subject:
            href += f"?subject={quote(subject)}"
        return f"[{label}]({href})"

    def _tel_link(value, label=None):
        if not value:
            return ""
        label = label or value
        sanitized = value.replace(" ", "")
        return f"[{label}](tel:{sanitized})"

    def _external_link(value, label=None):
        if not value:
            return ""
        label = label or value
        return f"[{label}]({value})"

    env.filters["mailto_link"] = _mailto_link
    env.filters["tel_link"] = _tel_link
    env.filters["external_link"] = _external_link
