"""turns erlang code with special comments into RST

expects something like this as input:

    %% here we define a types

    % this becomes a comment in the literal block
    -type my_lovely_type() :: {atom(), over_fences | type_dentist}.

    %% later we can even reference `my_lovely_type()`

and outputs two paragraphs and a literal block

this depends on the literal-ref role to make nice looking references to code
blocks
"""

import re


def parse_args():
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("in_file", type=argparse.FileType("r"))
    parser.add_argument("out_file", type=argparse.FileType("w"))

    return parser.parse_args()


rst_line_re = re.compile("^\s*%%[^%](.*)$")
type_re = re.compile("^\s*-type\s+([a-z][^(]+)\(\)")


def deliterate(in_f, out_f):
    out_f.write(".. default-role:: literal-ref\n\n")

    # accumulates lines which aren't turned into RST; these are then printed by
    # flush_code_block
    code_block = []

    seen_rst = False

    def flush_code_block():
        if not code_block:
            return

        if not seen_rst:
            code_block.clear()
            return

        # strip blank lines before/after
        while code_block and not code_block[0].strip():
            del code_block[0]
        while code_block and not code_block[-1].strip():
            del code_block[-1]

        if code_block:
            out_f.write("\n")

            # add references for types in this block
            for line in code_block:
                type_match = type_re.match(line)
                if type_match is not None:
                    out_f.write(f".. _{type_match.group(1)}():\n")

            out_f.write(".. code-block:: erlang\n\n")
            for line in code_block:
                out_f.write("   ")
                out_f.write(line)

        out_f.write("\n")

        code_block.clear()

    for line in in_f:
        rst_line_match = rst_line_re.match(line)
        if rst_line_match:
            flush_code_block()
            out_f.write(rst_line_match.group(1))
            out_f.write("\n")
            seen_rst = True
        else:
            code_block.append(line)

    flush_code_block()


def main(args):
    deliterate(args.in_file, args.out_file)


if __name__ == "__main__":
    main(parse_args())
