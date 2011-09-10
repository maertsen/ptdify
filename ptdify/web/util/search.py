from django.conf import settings
import web.models as models

class Search:
    @staticmethod
    def fromJSON(query):
        safelist = [c.__name__ for c in Meta.__subclasses__()]
        chunklist = [q.rsplit(',', 1) for q in query]

        found_new = False
        classified = list()
        remainder = ""

        for chunk in chunklist:
            text = chunk[0]
            meta = chunk[1].capitalize()

            if found_new or meta == "New" or meta == "Unknown":
                found_new = True
                remainder += (" " + text )
            elif not meta in safelist:
                raise ValueError("unknown meta type: %s" % meta)
            else:
                classified.append(Block(text, eval(meta)))

        return Search(classified, remainder)

    def __init__(self, classified, remainder):
        self.classified = classified
        self.remainder = remainder.strip()
        self.children = []

    def autoComplete(self, numResults):
        self._execute()
        return self.collect()[:numResults]

    def _execute(self):
        if not self.remainder:
            return # we are done recursing

        chunk = self.remainder.split(None, 1)[0]

        # search chunk for every meta type still in scope
        for meta in self.getSearchScope():
            # and create a child for each result
            for result in eval(meta).searchPrefix(chunk):
                classified = list(self.classified)
                classified.append(result)

                # handle case where a prefix of the remainder is contained
                # in the classified block
                newRemainder = self.remainder[len(result.text):]

                child = Search(classified, newRemainder)

                # recursively calling the child to execute as well
                child._execute()
                self.children.append(child)

    def collect(self):
        result = []

        if not len(self.children):
            result.append(self.classified)
        else:
            for c in self.children:
                result.extend(c.collect())

        return sorted(result, key=lambda x: reduce(lambda y,z: y+z.meta.weight, x, 0), reverse=True)

    def getSearchScope(self):
        types = [c.__name__ for c in Meta.__subclasses__()]

        if self.classified:
            return set(types).difference([b.meta for b in self.classified])
        else:
            return types

class Block:
    def __init__(self, text, meta):
        self.text = text
        self.meta = meta

    def __str__(self):
        return "text: '%s' meta: '%s'" % (self.text, self.meta.__class__.__name__)

    def as_list(self):
        return [self.text, self.meta.__class__.__name__]

"""
Placeholder for possible metadata attached to text
"""
class Meta(object):
    model = None
    weight = 1

    @classmethod
    def searchPrefix(cls, prefix):
        # search cls.model for prefix
        results = cls.model.objects.filter(name__istartswith=prefix).iterator()

        # create a block for each result
        blocks = []

        for r in results:
            blocks.append(Block(r.name, cls.__new__(cls)))

        return blocks

class Area(Meta):
    model = models.Area

class Contact(Meta):
    model = models.Contact

class Context(Meta):
    model = models.Context

class Project(Meta):
    model = models.Project

class Realm(Meta):
    model = models.Realm

class Keyword(Meta):
    # overwrite function to not use database
    @classmethod
    def searchPrefix(cls, prefix):

        blocks = list()
       
        keywordlist = [c.__name__ for c in Meta.__subclasses__()]
        # TODO move to some proper place
        # add special keyword
        keywordlist.append('Action')

        # search list of special words
        for m in keywordlist:
            if m.startswith(prefix.capitalize()):
               blocks.append(Block(m.lower(), cls.__new__(cls))) 

        return blocks

class Unknown(Meta):
    weight = -1

    @classmethod
    def searchPrefix(cls, prefix):
        return [Block(prefix, cls.__new__(cls))]
