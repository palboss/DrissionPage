# -*- coding:utf-8 -*-
"""
@Author  :   g1879
@Contact :   g1879@qq.com
"""
from typing import Union, List, Any, Tuple

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from .base import BasePage
from .driver_element import DriverElement, Scroll, ElementWaiter
from .mix_page import MixPage
from .session_element import SessionElement


class DriverPage(BasePage):

    def __init__(self, driver: RemoteWebDriver, timeout: float = 10) -> None:
        self._driver: RemoteWebDriver = ...
        self._url: str = ...
        self._wait_object: WebDriverWait = ...
        self._scroll: Scroll = ...

    def __call__(self, loc_or_str: Union[Tuple[str, str], str, DriverElement, WebElement],
                 timeout: float = None) -> Union[DriverElement, str, None]: ...

    # -----------------共有属性和方法-------------------
    @property
    def url(self) -> Union[str, None]: ...

    @property
    def html(self) -> str: ...

    @property
    def json(self) -> dict: ...

    def get(self,
            url: str,
            show_errmsg: bool = False,
            retry: int = None,
            interval: float = None) -> Union[None, bool]: ...

    def ele(self,
            loc_or_ele: Union[Tuple[str, str], str, DriverElement, WebElement],
            timeout: float = None) -> Union[DriverElement, str, None]: ...

    def eles(self,
             loc_or_str: Union[Tuple[str, str], str],
             timeout: float = None) -> List[Union[DriverElement, str]]: ...

    def s_ele(self, loc_or_ele: Union[Tuple[str, str], str, DriverElement] = None) \
            -> Union[SessionElement, str, None]: ...

    def s_eles(self, loc_or_str: Union[Tuple[str, str], str]) -> List[Union[SessionElement, str]]: ...

    def _ele(self,
             loc_or_ele: Union[Tuple[str, str], str, DriverElement, WebElement],
             timeout: float = None,
             single: bool = True) -> Union[DriverElement, str, None, List[Union[DriverElement, str]]]: ...

    def get_cookies(self, as_dict: bool = False) -> Union[list, dict]: ...

    @property
    def timeout(self) -> float: ...

    @timeout.setter
    def timeout(self, second: float) -> None: ...

    def _d_connect(self,
                   to_url: str,
                   times: int = 0,
                   interval: float = 1,
                   show_errmsg: bool = False) -> Union[bool, None]: ...

    # ----------------driver独有属性和方法-----------------------
    @property
    def driver(self) -> WebDriver: ...

    @property
    def wait_object(self) -> WebDriverWait: ...

    @property
    def timeouts(self) -> dict: ...

    @property
    def tabs_count(self) -> int: ...

    @property
    def tab_handles(self) -> list: ...

    @property
    def current_tab_index(self) -> int: ...

    @property
    def current_tab_handle(self) -> str: ...

    @property
    def active_ele(self) -> DriverElement: ...

    @property
    def scroll(self) -> Scroll: ...

    @property
    def to_frame(self) -> ToFrame: ...

    def set_timeouts(self, implicit: float = None, pageLoad: float = None, script: float = None) -> None: ...

    def wait_ele(self,
                 loc_or_ele: Union[str, tuple, DriverElement, WebElement],
                 timeout: float = None) -> ElementWaiter: ...

    def check_page(self) -> Union[bool, None]: ...

    def run_script(self, script: str, *args) -> Any: ...

    def run_async_script(self, script: str, *args) -> Any: ...

    def run_cdp(self, cmd: str, **cmd_args) -> Any: ...

    def create_tab(self, url: str = '') -> None: ...

    def close_tabs(self, num_or_handles: Union[int, str, list, tuple] = None) -> None: ...

    def close_other_tabs(self, num_or_handles: Union[int, str, list, tuple] = None) -> None: ...

    def to_tab(self, num_or_handle: Union[int, str] = 0) -> None: ...

    def set_ua_to_tab(self, ua: str) -> None: ...

    def get_session_storage(self, item: str = None) -> Union[str, dict, None]: ...

    def get_local_storage(self, item: str = None) -> Union[str, dict, None]: ...

    def set_session_storage(self, item: str, value: Union[str, bool]) -> None: ...

    def set_local_storage(self, item: str, value: Union[str, bool]) -> None: ...

    def clean_cache(self,
                    session_storage: bool = True,
                    local_storage: bool = True,
                    cache: bool = True,
                    cookies: bool = True) -> None: ...

    def screenshot(self, path: str = None, filename: str = None, as_bytes: bool = False) -> Union[str, bytes]: ...

    def scroll_to_see(self, loc_or_ele: Union[str, tuple, WebElement, DriverElement]) -> None: ...

    def refresh(self) -> None: ...

    def stop_loading(self) -> None: ...

    def back(self) -> None: ...

    def forward(self) -> None: ...

    def set_window_size(self, width: int = None, height: int = None) -> None: ...

    def chrome_downloading(self, download_path: str) -> list: ...

    def process_alert(self, ok: bool = True, send: str = None, timeout: float = None) -> Union[str, None]: ...


class ToFrame(object):

    def __init__(self, page: DriverPage):
        self.page: DriverPage = ...

    def __call__(self, condition: Union[int, str, tuple, WebElement, DriverElement] = 'main') -> Union[
        DriverPage, MixPage]: ...

    def main(self) -> DriverPage: ...

    def parent(self, level: int = 1) -> DriverPage: ...

    def by_id(self, id_: str) -> DriverPage: ...

    def by_name(self, name: str) -> DriverPage: ...

    def by_index(self, index: int) -> DriverPage: ...

    def by_loc(self, loc: Union[str, tuple]) -> DriverPage: ...

    def by_ele(self, ele: Union[DriverElement, WebElement]) -> DriverPage: ...


def get_handles(handles: list, num_or_handles: Union[int, str, list, tuple]) -> set: ...