# Copyright 2022 XProbe Inc.
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

from xorbits.core.adapter import (
    mars_flatiter,
    register_converter,
    to_mars,
    wrap_mars_callable,
)


@register_converter(from_cls_list=[mars_flatiter])
class FlatIter:
    def __init__(self, mars_obj: "mars_flatiter"):
        self._mars_obj = mars_obj

    def __getitem__(self, item):
        return wrap_mars_callable(
            self._mars_obj.__getitem__, attach_docstring=False, is_method=True
        )(item)

    def __setitem__(self, key, value):
        self._mars_obj[key] = to_mars(value)