# -*- coding: utf-8 -*-

# AlFeedback
# Simple scriptfilter feedback for Alfred 2.
# Franz Heidl 2013
# http://github.com/franzheidl/
# MIT license.


from xml.etree import ElementTree as eTree
import time

class Feedback:

    def __init__(self, *items):
        self.feedback = eTree.Element('items')
        # Add items on init, expects list of dicts representing on item each:
        if items:
            for item in items:
                self.addItem(**item)


    def addItem(self, **kwargs):
        # Create Item
        item = eTree.SubElement(self.feedback, 'item')

        # Set Item Attributes
        if 'valid' in kwargs.keys():
            item.set('valid', kwargs['valid'])
        if 'arg' in kwargs.keys():
            item.set('arg', kwargs['arg'])
        if 'autocomplete' in kwargs.keys():
            item.set('autocomplete', kwargs['autocomplete'])
        if 'type' in kwargs.keys():
            item.set('type', kwargs['type'])
        if 'uid' in kwargs.keys():
            if kwargs.get('uid') == 'timestamp':
                item.set('uid', self.timestamp())
            else:
                item.set('uid', kwargs['uid'])

        # Create Item Elements
        if 'title' in kwargs.keys():
            title = eTree.SubElement(item, 'title')
            title.text = kwargs['title']
        if 'subtitle' in kwargs.keys():
            subtitle = eTree.SubElement(item, 'subtitle')
            subtitle.text = kwargs['subtitle']
        if 'icon' in kwargs.keys():
            icon = eTree.SubElement(item, 'icon')
            icon.text = kwargs['icon']
        if 'icontype' in kwargs.keys():
            icon.set('type', kwargs['icontype'])


    def timestamp(self):
        return time.strftime('%Y-%m-%d-%H%M%S%Z')

    def __repr__(self):
        return eTree.tostring(self.feedback, encoding="utf-8")
