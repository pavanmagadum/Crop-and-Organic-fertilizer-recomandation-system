import glob
import io
import os

def main(root='.'):
    # Find all .md files under root, excluding the combined file itself
    pattern = os.path.join(root, '**', '*.md')
    files = sorted(glob.glob(pattern, recursive=True))
    out_path = os.path.join(root, 'ALL_MARKDOWN_COMBINED.md')
    files = [f for f in files if os.path.normpath(f) != os.path.normpath(out_path)]

    with io.open(out_path, 'w', encoding='utf-8') as out:
        out.write('# ALL_MARKDOWN_COMBINED.md\n')
        out.write('\n')
        for path in files:
            rel = os.path.relpath(path, start=root)
            out.write('## File: {}\n\n'.format(rel.replace('\\', '/')))
            try:
                with io.open(path, 'r', encoding='utf-8') as fh:
                    out.write(fh.read())
            except Exception as e:
                out.write(f"<!-- Failed to read {rel}: {e} -->\n")
            out.write('\n\n---\n\n')

    print('Wrote', out_path)

if __name__ == '__main__':
    main(os.path.dirname(os.path.dirname(__file__)))
