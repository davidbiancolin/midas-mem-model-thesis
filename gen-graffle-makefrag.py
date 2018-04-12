import re
import glob

# Whatever follows '% graffle2pdf' will be passed directly to omnigraffle-export
omnigraffle_re = re.compile(r'%\s*graffle2pdf -c ([^\s]*)\s*([^\s]*)\s*([^\s]*)')

MAKEFRAG_NAME = 'graffle-figures.mk'
FIGURE_LIST_MAKEVAR = 'graffle_figures'

def gen_pdf_list(figs):
  """
  Generate a make variable with all of the generated pdf names
  """

  assert figs is not None
  pdfs = "{} := {}".format(FIGURE_LIST_MAKEVAR, figs[0][2])
  for fig in figs[1:]:
    pdfs += " \\\n\t{}".format(fig[2])

  return pdfs + "\n"

def gen_makefrag_recipe(arguments):
  """
  Generate a recipe for this pdf.
  """
  canvas_name   = arguments[0]
  input_graffle = arguments[1]
  output_name   = arguments[2]
  recipe = """
{}:{}
\tomnigraffle-export -c {} {} {}
""".format(output_name, input_graffle, *arguments)

  return recipe

if __name__ == "__main__":

  fnames = glob.glob("tex/*.tex")
  figures = []
  for fname in fnames:
    with open(fname) as f:
      for l in f:
          m = omnigraffle_re.match(l.strip())
          if m:
              figures += [m.groups()]

  with open(MAKEFRAG_NAME, 'wb') as f:
    f.write(gen_pdf_list(figures))
    for fig in figures:
      f.write(gen_makefrag_recipe(fig))
