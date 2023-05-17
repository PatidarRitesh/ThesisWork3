# Author name - ACL/ACM

/{person}{([A-Za-z0-9\s~.]+)([\\'{"a-zA-Z0-9}\s-]*)}/g

or 

/{person}{([A-Za-z0-9\s~.]+)({[\\'\w\d\s"-]+}[\d\w\s-]*)*/g

If the group 2 contains any data that means the it is incorrect name 
and we just copy paste it as it is by merging both the groups 

# Year ACM/ACL

/\((\d{4})\)|({\d{4}})/g

We can use either of one grp


# BIB ID ACM/ACL

/\]% {([\w\d\s:\/-]+)}/g

-----------------------------------------------------------------------

# Title 

## ACM/ACL

### articletitle 

/\\showarticletitle{([\w\d\s:{},.-]*)}/gm


#### ERROR PATTERN 

> \\showarticletitle{([\w\d\s:{},.";'“”-]*(\&)*)*}


```

\showarticletitle{Wide \& deep learning for recommender systems}. In \bibinfo{booktitle}{\emph{1st DLRS workshop}}.


\showarticletitle{A note on the definition of “dual use”}.

\showarticletitle{Give Me Convenience and Give Her Death: Who Should Decide What Uses of {NLP} are Appropriate, and on What Basis?}. df\

\\showarticletitle{([\w\d\s:{},.";'“”-]*)}

TITLE:  \showarticletitle{Give Me Convenience and Give Her Death: Who Should Decide What Uses of {NLP} are Appropriate, and on What Basis?}. In \bibinfo{booktitle}{\emph{Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, {ACL} 2020, Online, July 5-10, 2020}}, \bibfield{editor}{\bibinfo{person}{Dan Jurafsky}, \bibinfo{person}{Joyce Chai}, \bibinfo{person}{Natalie Schluter}, {and} \bibinfo{person}{Joel~R. Tetreault}} (Eds.). \bibinfo{publisher}{Association for Computational Linguistics}, \bibinfo{pages}{2908--2913}.       


```

### Booktitle 1

/booktitle}{\\emph{([\w\s:,{}*;"'()\/-]+)}}/gm

### Publisher 

/bibinfo{publisher}{{?([\w\s]+)/gm

### Page(s)

/bibinfo{pages}{(\d+)(-+)?(\d*)/gm

## Input/IEEE/CVPR  (Title/Link)

/((\bhttps:.+)}\s{)?|([\w\s,'":\/—-]*)/gm

----------------------------------------------------------------------

# Publication 

## ACM/ACL

### Journal

ACL has the URLs in the publication section so we can use the same regex for both the cases
ACM has only Journals

/journal}{\\emph{([\w\s.]+)|url{([^}]*)}/gm

### Year

/bibinfo{year}{(\d{4})/gm

### Volume
/bibinfo{volume}{(\d+)/gm

### Page(s)

/bibinfo{pages}{(\d+)(-+)?(\d*)/gm

## Input/IEEE/CVPR

### Publication Name 

/em[ph{\s]+([^}]+)/gm

### Page(s)

/(\d+)-+(\d+)/gm



# Problems encountered while creating REGEX

```
[Forge(2010)]%
        {forge2010note}
\\bibfield{author}{\\bibinfo{person}{John Forge}.}
  \\bibinfo{year}{2010}\\natexlab{}.
\\newblock \\showarticletitle{A note on the definition of “dual use”}.
\\newblock \\bibinfo{journal}{\emph{Science and Engineering Ethics}}
  \\bibinfo{volume}{16}, \\bibinfo{number}{1} (\\bibinfo{year}{2010}),
  \\bibinfo{pages}{111--118}.
\\newblock
```

> Pattern `\\showarticletitle{(([\w\d\s:{},.-]*(\\&)?)+)}`

# without newblock pattern

## for publication

/emph{([^}]*)/gm

## for id 

/bibitem{([^}]*)/gm

## for title

/``([^'']*)/gm

## for authors name 

/bibitem{[\w\d\s:'^%.,]*} ([^``]*)/gm

## for volume

/vol.[~\s](\d*)/gm




