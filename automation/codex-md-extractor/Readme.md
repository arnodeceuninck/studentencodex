The codex was given in `docx` format, with strange formatting. Some titles were an actual title, others were page headers, making it difficult to identify different songs. 

Following steps made it easier:
- Convert the `.docx` to a `pdf`: https://www.ilovepdf.com/word_to_pdf
- Convert the `pdf` back to `.docx`: https://pdf2docx.com/

This gave a `docx` file with all song titles as actual titles. 

Use [pandoc](https://github.com/jgm/pandoc) to convert the `docx` to `md`
```shell
pandoc -o codex.md codex.docx
```

This gives everything as one large Markdown file. `codex-md-extractor.py` converts this large Markdown file into files of the format needed for the application. 