
class Institution(object):
    institution_name = None
    website = None
    industry = None
    type = None
    headquarters = None
    company_size = None
    founded = None

    def __init__(self, name=None, website=None, industry=None, type=None, headquarters=None, company_size=None, founded=None):
        self.name = name
        self.website = website
        self.industry = industry
        self.type = type
        self.headquarters = headquarters
        self.company_size = company_size
        self.founded = founded

class Experience(Institution):
    from_date = None
    to_date = None
    description = None
    position_title = None
    duration = None

    def __init__(self, from_date = None, to_date = None, description = None, position_title = None, duration = None, location = None):
        self.from_date = from_date
        self.to_date = to_date
        self.description = description
        self.position_title = position_title
        self.duration = duration
        self.location = location

    def __repr__(self):
        return "{position_title} at {company} from {from_date} to {to_date} for {duration} based at {location}".format( from_date = self.from_date, to_date = self.to_date, position_title = self.position_title, company = self.institution_name, duration = self.duration, location = self.location)
    def __str__(self):
        return "{company}, {location}\n  {position_title}\n{from_date} - {to_date}".format( from_date = self.from_date, to_date = self.to_date, position_title = ('\n').join(self.position_title), company = self.institution_name, location = list(set(self.location)))

class Education(Institution):
    from_date = None
    to_date = None
    description = None
    degree = None

    def __init__(self, from_date = None, to_date = None, description = None, degree = None):
        self.from_date = from_date
        self.to_date = to_date
        self.description = description
        self.degree = degree

    def __repr__(self):
        return "{degree} at {company} from {from_date} to {to_date}".format( from_date = self.from_date, to_date = self.to_date, degree = self.degree, company = self.institution_name)
    def __str__(self):
        return "{company}, {degree}\n{from_date} - {to_date}".format( from_date = self.from_date[-2:], to_date = self.to_date[-2:], degree = self.degree, company = self.institution_name)



class Scraper(object):
    driver = None

    def is_signed_in(self):
        try:
            self.driver.find_element_by_id("profile-nav-item")
            return True
        except:
            pass
        return False

    def __find_element_by_class_name__(self, class_name):
        try:
            self.driver.find_element_by_class_name(class_name)
            return True
        except:
            pass
        return False
