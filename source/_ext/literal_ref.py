from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole


class LiteralRefRole(SphinxRole):
    """a reference that is rendered as a literal"""

    def run(self):
        node = nodes.reference("", "", refname=self.text)
        node += nodes.literal(text=self.text)

        return [node], []


def setup(app: Sphinx):
    app.add_role("literal-ref", LiteralRefRole())

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
