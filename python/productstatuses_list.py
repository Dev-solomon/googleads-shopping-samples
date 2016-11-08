#!/usr/bin/python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Gets the status of all products on the specified account."""

import sys

from oauth2client import client
import shopping_common

# The maximum number of results to be returned in a page.
MAX_PAGE_SIZE = 50


def main(argv):
  # Authenticate and construct service.
  service, config, _ = shopping_common.init(argv, __doc__)
  merchant_id = config['merchantId']
  shopping_common.check_mca(config, False)

  try:
    request = service.productstatuses().list(
        merchantId=merchant_id, maxResults=MAX_PAGE_SIZE)

    while request is not None:
      result = request.execute()
      if 'resources' in result:
        statuses = result['resources']
        for status in statuses:
          print ('- Product "%s" with title "%s":' %
                 (status['productId'], status['title']))
          if not status['dataQualityIssues']:
            print '  No data quality issues.'
          else:
            print('  Found %d data quality issues:' %
                  len(status['dataQualityIssues']))
            for issue in status['dataQualityIssues']:
              if 'detail' in issue:
                print('  - (%s) [%s] %s' %
                      (issue['severity'], issue['id'], issue['detail']))
              else:
                print '  - (%s) [%s]' % (issue['severity'], issue['id'])

        request = service.productstatuses().list_next(request, result)
      else:
        print 'No products were found.'
        break

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
