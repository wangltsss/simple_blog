---
title: Latex Basics
date: 2023-05-10
---

# LaTex Basics and Cheat Sheet  

This blog serves as a concise summary of essential LaTex features along with a handy cheat sheet. If you're looking for an in-depth tutorial or a comprehensive guide on the advantages of using LaTex, this blog may not cover all your needs. Instead, it provides a quick reference to help you effectively utilize LaTex in your projects.


## Table of Contents

1. [Getting Started with LaTeX](#getting-started-with-latex)
2. [Writing Text and Formatting](#writing-text-and-formatting)
3. [Lists](#lists)
4. [Including Mathematics](#including-mathematics)
5. [Adding Figures and Tables](#adding-figures-and-tables)
6. [LaTeX Cheat Sheet](#latex-cheat-sheet)


## Getting Started with LaTeX

Every LaTeX document follows a basic structure:

```latex
\documentclass{article} % Document class

\usepackage[utf8]{inputenc} % Encoding

\title{Your Document Title}
\author{Your Name}
\date{\today}

\begin{document}

\maketitle % Generates the title

\section{Introduction}
Your introductory text goes here.

\section{Main Content}
Details of your main content.

\subsection{Subsection}
Further details.

\end{document}
```

## Writing Text and Formatting

LaTeX provides a range of commands to format your text:

- **Bold Text:** `\textbf{This is bold text.}`
- *Italic Text:* `\textit{This is italic text.}`
- <ins>Underlined Text</ins>: `\underline{This is underlined text.}`
- ~~Strikethrough Text~~: `\sout{This text is struck through.}` *(Requires the `ulem` package)*

### Lists:

- **Itemized List:**

  ```latex
  \begin{itemize}
    \item First item
    \item Second item
    \item Third item
  \end{itemize}
  ```

- **Enumerated List:**

  ```latex
  \begin{enumerate}
    \item First item
    \item Second item
    \item Third item
  \end{enumerate}
  ```

- **Description List:**

  ```latex
  \begin{description}
    \item[Term 1] Description for term 1.
    \item[Term 2] Description for term 2.
  \end{description}
  ```

## Including Mathematics

One of LaTeX's standout features is its ability to handle complex mathematical expressions with ease.

- **Inline Math:** Use `$ ... $` to include math within a line of text. Example: `$E = mc^2$` renders as \(E = mc^2\).
- **Displayed Equations:** Use `\[ ... \]` for equations on their own line.
  
  ```latex
  \[
  \int_{a}^{b} f(x) \, dx
  \]
  ```

- **Equation Environment:** For numbering equations.
  
  ```latex
  \begin{equation}
  E = mc^2
  \end{equation}
  ```

- **Align Environment:** For aligning multiple equations.
  
  ```latex
  \begin{align}
  a &= b + c \\
  d &= e - f
  \end{align}
  ```

## Adding Figures and Tables

Inserting images and tables enhances the clarity and professionalism of your documents.

- **Figures:**
  
  ```latex
  \begin{figure}[h]
    \centering
    \includegraphics[width=0.5\textwidth]{path/to/image.png}
    \caption{Caption for the image.}
    \label{fig:image_label}
  \end{figure}
  ```

- **Tables:**
  
  ```latex
  \begin{table}[h]
    \centering
    \begin{tabular}{|c|c|c|}
      \hline
      Column1 & Column2 & Column3 \\
      \hline
      Data1 & Data2 & Data3 \\
      Data4 & Data5 & Data6 \\
      \hline
    \end{tabular}
    \caption{Caption for the table.}
    \label{tab:table_label}
  \end{table}
  ```

## LaTeX Cheat Sheet

Navigating LaTeX's commands can be daunting for beginners. Here's a comprehensive cheat sheet listing common LaTeX commands (often referred to as "tags") to help you get up to speed quickly:

### Document Structure

| **Command**               | **Purpose**                                                  | **Example**                           |
|---------------------------|--------------------------------------------------------------|---------------------------------------|
| `\documentclass{}`        | Specifies the type of document (e.g., article, book)         | `\documentclass{report}`              |
| `\usepackage{}`            | Imports a package to extend functionality                   | `\usepackage{graphicx}`                |
| `\begin{document}`        | Starts the content of the document                           | `\begin{document}`                     |
| `\end{document}`          | Ends the content of the document                             | `\end{document}`                       |
| `\title{}`                | Sets the document title                                      | `\title{My First Document}`            |
| `\author{}`               | Sets the author name                                         | `\author{Jane Doe}`                    |
| `\date{}`                 | Sets the date; use `\today` for current date                 | `\date{\today}`                        |
| `\maketitle`              | Generates the title section                                  | `\maketitle`                           |

### Sections and Subsections

| **Command**               | **Purpose**                                                  | **Example**                           |
|---------------------------|--------------------------------------------------------------|---------------------------------------|
| `\section{}`              | Creates a new section                                       | `\section{Introduction}`               |
| `\subsection{}`           | Creates a subsection                                        | `\subsection{Background}`              |
| `\subsubsection{}`        | Creates a subsubsection                                     | `\subsubsection{Details}`              |
| `\paragraph{}`            | Creates a paragraph heading                                 | `\paragraph{Overview}`                 |
| `\subparagraph{}`         | Creates a subparagraph heading                              | `\subparagraph{Scope}`                 |

### Text Formatting

| **Command**               | **Purpose**                                                  | **Example**                           |
|---------------------------|--------------------------------------------------------------|---------------------------------------|
| `\textbf{}`               | Makes text bold                                             | `\textbf{Bold Text}`                   |
| `\textit{}`               | Makes text italic                                           | `\textit{Italic Text}`                 |
| `\underline{}`            | Underlines text                                             | `\underline{Underlined Text}`          |
| `\sout{}`                 | Strikethrough text (requires `ulem` package)               | `\sout{Strikethrough}`                 |
| `\emph{}`                 | Emphasizes text (usually italics)                           | `\emph{Emphasized Text}`               |
| `\texttt{}`               | Typesets text in monospaced (typewriter) font               | `\texttt{Code Snippet}`                |
| `\textcolor{color}{}`     | Changes text color (requires `xcolor` package)             | `\textcolor{red}{Red Text}`            |

### Lists

| **Command**               | **Purpose**                                                  | **Example**                           |
|---------------------------|--------------------------------------------------------------|---------------------------------------|
| `\begin{itemize}`         | Starts an unordered (bullet) list                           | See above for itemized list example   |
| `\end{itemize}`           | Ends an unordered list                                      |                                       |
| `\begin{enumerate}`       | Starts an ordered (numbered) list                           | See above for enumerated list example |
| `\end{enumerate}`         | Ends an ordered list                                        |                                       |
| `\begin{description}`     | Starts a description list                                   | See above for description list example |
| `\end{description}`       | Ends a description list                                     |                                       |
| `\item`                   | Adds an item to a list                                      | `\item First item`                     |

### Mathematics

| **Command**               | **Purpose**                                                  | **Example**                           |
|---------------------------|--------------------------------------------------------------|---------------------------------------|
| `$ ... $`                 | Inline math mode                                            | `$E = mc^2$`                           |
| `\[ ... \]`               | Displayed math mode                                         | `\[\int_a^b f(x) \, dx\]`              |
| `\begin{equation}`        | Starts a numbered equation                                  | See above for equation example        |
| `\end{equation}`          | Ends a numbered equation                                    |                                       |
| `\begin{align}`           | Starts an aligned set of equations                          | See above for align example           |
| `\end{align}`             | Ends an aligned set of equations                            |                                       |
| `\frac{}{}`               | Creates a fraction                                           | `\frac{a}{b}`                           |
| `\sqrt{}`                 | Creates a square root                                       | `\sqrt{x}`                             |
| `^` and `_`               | Superscript and subscript                                   | `x^2`, `a_i`                            |
| `\sum`, `\int`, `\lim`    | Summation, integral, limit symbols                          | `\sum_{i=1}^n`, `\int_a^b`             |
| `\alpha`, `\beta`, etc.   | Greek letters                                               | `\alpha + \beta`                       |

### Figures and Tables

| **Command**               | **Purpose**                                                  | **Example**                           |
|---------------------------|--------------------------------------------------------------|---------------------------------------|
| `\begin{figure}[placement]` | Starts a figure environment                                | See above for figure example          |
| `\end{figure}`             | Ends a figure environment                                   |                                       |
| `\includegraphics{}`        | Includes an image (requires `graphicx` package)            | `\includegraphics[width=0.5\textwidth]{image.png}` |
| `\caption{}`                | Adds a caption to a figure or table                        | `\caption{Sample Figure}`              |
| `\label{}`                  | Labels a figure or table for referencing                   | `\label{fig:sample}`                   |
| `\begin{table}[placement]`  | Starts a table environment                                 | See above for table example           |
| `\end{table}`               | Ends a table environment                                   |                                       |
| `\begin{tabular}{columns}`  | Starts a tabular environment with specified column format  | `\begin{tabular}{|c|c|c|}`             |
| `\end{tabular}`             | Ends a tabular environment                                 |                                       |
| `\hline`                    | Adds a horizontal line in tables                            | Used within `tabular`                  |
| `&`                         | Separates columns in tables                                 | `Data1 & Data2 & Data3`                |
| `\\`                        | Ends a row in tables or breaks lines                       | `Data1 & Data2 & Data3 \\`             |

### Cross-Referencing

| **Command**               | **Purpose**                                                  | **Example**                           |
|---------------------------|--------------------------------------------------------------|---------------------------------------|
| `\label{}`                 | Assigns a label to a section, figure, table, etc.           | `\label{sec:intro}`                    |
| `\ref{}`                   | References the labeled item                                | `As seen in Section~\ref{sec:intro}`   |
| `\pageref{}`               | References the page number of the labeled item             | `See page~\pageref{sec:intro}`         |
| `\cite{}`                  | Cites a bibliography entry                                 | `\cite{smith2020}`                      |
| `\bibliographystyle{}`     | Specifies the bibliography style                           | `\bibliographystyle{plain}`             |
| `\bibliography{}`          | Includes the bibliography file                             | `\bibliography{references}`             |

### Custom Commands and Environments

| **Command**               | **Purpose**                                                  | **Example**                           |
|---------------------------|--------------------------------------------------------------|---------------------------------------|
| `\newcommand{}`            | Defines a new command                                      | `\newcommand{\R}{\mathbb{R}}`          |
| `\renewcommand{}`          | Redefines an existing command                              | `\renewcommand{\baselinestretch}{1.5}`  |
| `\newenvironment{}`       | Defines a new environment                                   | `\newenvironment{myenv}{...}{...}`    |
| `\renewenvironment{}`     | Redefines an existing environment                           | `\renewenvironment{quote}{...}{...}`  |

### Miscellaneous

| **Command**               | **Purpose**                                                  | **Example**                           |
|---------------------------|--------------------------------------------------------------|---------------------------------------|
| `\footnote{}`              | Adds a footnote                                           | `This is a footnote\footnote{Footnote text.}` |
| `\tableofcontents`         | Generates a table of contents                              | `\tableofcontents`                     |
| `\listoffigures`           | Generates a list of figures                                | `\listoffigures`                       |
| `\listoftables`            | Generates a list of tables                                 | `\listoftables`                        |
| `\clearpage`               | Ends the current page and flushes all pending floats       | `\clearpage`                           |
| `\newline`                 | Inserts a line break                                      | `First line.\newline Second line.`     |
| `\pagebreak`               | Suggests a page break                                     | `\pagebreak`                           |

### Packages

Packages extend LaTeX's functionality. Here are some commonly used ones:

| **Package**               | **Purpose**                                                  | **Usage**                           |
|---------------------------|--------------------------------------------------------------|-------------------------------------|
| `graphicx`                 | Includes images and graphics                             | `\usepackage{graphicx}`              |
| `amsmath`                 | Enhanced mathematical typesetting                        | `\usepackage{amsmath}`                |
| `amssymb`                 | Additional mathematical symbols                           | `\usepackage{amssymb}`                |
| `geometry`                | Customizes page layout and margins                        | `\usepackage{geometry}`               |
| `xcolor`                  | Adds color to text and elements                            | `\usepackage{xcolor}`                 |
| `hyperref`                | Creates hyperlinks within the document                     | `\usepackage{hyperref}`               |
| `babel`                   | Supports multilingual typesetting                          | `\usepackage[english]{babel}`         |
| `fontenc`                 | Specifies font encoding                                   | `\usepackage[T1]{fontenc}`            |
| `inputenc`                | Specifies input encoding                                 | `\usepackage[utf8]{inputenc}`         |
| `biblatex`                | Advanced bibliography management                           | `\usepackage{biblatex}`                |
| `booktabs`                | Enhances table formatting                                  | `\usepackage{booktabs}`                |

