# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class Offer(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isOffer = True
        super(Offer, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        claim_limit = 'claim_limit'
        coupon_type = 'coupon_type'
        created_time = 'created_time'
        expiration_time = 'expiration_time'
        field_from = 'from'
        id = 'id'
        image_url = 'image_url'
        message = 'message'
        redemption_code = 'redemption_code'
        redemption_link = 'redemption_link'
        terms = 'terms'
        title = 'title'

    def api_get(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='GET',
            endpoint='/',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Offer,
            api_type='NODE',
            response_parser=ObjectParser(reuse_object=self),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_comment(self, fields=None, params=None, batch=None, pending=False):
        from facebook_business.adobjects.comment import Comment
        param_types = {
            'object_id': 'string',
            'parent_comment_id': 'Object',
            'nectar_module': 'string',
            'attachment_id': 'string',
            'attachment_url': 'string',
            'attachment_share_url': 'string',
            'feedback_source': 'string',
            'facepile_mentioned_ids': 'list<string>',
            'is_offline': 'bool',
            'comment_privacy_value': 'comment_privacy_value_enum',
            'message': 'string',
            'text': 'string',
            'tracking': 'string',
        }
        enums = {
            'comment_privacy_value_enum': Comment.CommentPrivacyValue.__dict__.values(),
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/comments',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Comment,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Comment, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def delete_likes(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'tracking': 'string',
            'nectar_module': 'string',
            'notify': 'bool',
            'feedback_source': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='DELETE',
            endpoint='/likes',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=AbstractCrudObject,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=AbstractCrudObject, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    def create_like(self, fields=None, params=None, batch=None, pending=False):
        param_types = {
            'tracking': 'string',
            'nectar_module': 'string',
            'notify': 'bool',
            'feedback_source': 'string',
        }
        enums = {
        }
        request = FacebookRequest(
            node_id=self['id'],
            method='POST',
            endpoint='/likes',
            api=self._api,
            param_checker=TypeChecker(param_types, enums),
            target_class=Offer,
            api_type='EDGE',
            response_parser=ObjectParser(target_class=Offer, api=self._api),
        )
        request.add_params(params)
        request.add_fields(fields)

        if batch is not None:
            request.add_to_batch(batch)
            return request
        elif pending:
            return request
        else:
            self.assure_call()
            return request.execute()

    _field_types = {
        'claim_limit': 'unsigned int',
        'coupon_type': 'string',
        'created_time': 'datetime',
        'expiration_time': 'datetime',
        'from': 'Page',
        'id': 'string',
        'image_url': 'string',
        'message': 'string',
        'redemption_code': 'string',
        'redemption_link': 'string',
        'terms': 'string',
        'title': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info


