from html import escape

from docutils import nodes
from docutils.parsers.rst import Directive

class kalturaVideoDirective(Directive):
    """create a placeholder for a kaltura video"""

    required_arguments = 1
    has_content = False

    def run(self):
        entry_id = self.arguments[0].strip()

        video_number = self.state.document.settings.env.new_serialno('kaltura_video')
        target_id = f'kaltura-video-{video_number}'

        html = (
            f'<div id="{target_id}" '
            f'class="kaltura-video-player" '
            f'data-entry-id="{escape(entry_id, quote=True)}">'
            "</div>"
        )

        return [nodes.raw("", html, format="html")]