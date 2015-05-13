from django.db import models


class Profile(models.Model):
    user = models.CharField(max_length=100, unique=True)
    f_name = models.CharField(max_length=100)
    m_name = models.CharField(max_length=100,)
    l_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    # profile_pic = models.ForeignKey('Comment', related_name='profile_pic', default='static/images/default')
    MALE='M'
    FEMALE='F'
    OTHER='O'
    SEX = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER,'Other'),
        (None,'')
    )
    gender = models.CharField(choices=SEX,default=None,max_length=1)

    def __unicode__(self):
        return self.user

class Comment(models.Model):
    user = models.ForeignKey(Profile, related_name='op')
    comment = models.BinaryField()
    commenter = models.ForeignKey(Profile, related_name='commenter')
    parent = models.ForeignKey('self', related_name='parent_comment',db_constraint=False)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)

    def __unicode__(self):
        return self.id

class Contact(models.Model):
    user = models.ForeignKey(Profile, related_name='users_contact')
    contact = models.ForeignKey(Profile, related_name='contact')
    FRIEND = 'F'
    FOE = 'FO'
    BLOCKED = 'B'
    NA = 'NA'
    STATUS = (
        (FRIEND, 'Friend'),
        (FOE, 'Foe'),
        (BLOCKED, 'Blocked'),
        (NA, 'Not Accepted')
    )
    status = models.CharField(choices=STATUS,default=NA,max_length=2)

    def __unicode__(self):
        return self.contact