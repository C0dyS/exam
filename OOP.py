from datetime import datetime

class WebSite:
    def __init__(self, site_name, url, page_dict=None):
        self._site_name = site_name
        self._url = url
        if page_dict is None:
            self._page_dict = {}
        else:
            self._page_dict = page_dict

    def page_append(self, new_page_name, new_page_info):
        self._page_dict[new_page_name] = new_page_info


    def remove_page(self, page_to_remove_name):
        if page_to_remove_name in self._page_dict:
            del self._page_dict[page_to_remove_name]
            print(f"Page '{page_to_remove_name}' removed")
        else:
            print(f"Page '{page_to_remove_name}' does not exist")


    def display_info(self):
        print(f'site name: {self._site_name}')
        print(f'site URL: {self._url}')
        for page_name, page_info in self._page_dict.items():
            print(f'{page_name} page info : {page_info}')




class WebPage:
    def __init__(self,page_name,page_info,date_of_creation):
        self._page_name = page_name
        self._page_info = page_info
        self._date_of_creation = date_of_creation

    def display_info(self):
        print(f'page {self._page_name} has been created {self._date_of_creation}')
        print(f'page contents: {self._page_info}')

    def WebPageToWebSiteConvert(self):
        temporal_dict = {self._page_name: [self._page_info,self._date_of_creation]}
        return temporal_dict


def site_interactive_interface():
    web_site_instance = input('please enter existing site name you are going to be working with')
    while True:
        user_choice = input('''
        Please type :
        1 - to create a new site
        2 - to add a new page(using WebPage instance)
        3 - to remove a page
        4 - to check site info
        5 - to create a new page
        6 - to check your page info      
        7 - to exit
        
        ''')

        if user_choice == '1':
            site_name = input('Please enter the site name: ')
            site_url = input('Please enter the site URL: ')
            web_site_instance = WebSite(site_name,site_url)

        elif user_choice == '2':
            new_page_instance = input('Please enter your page instance name')
            temporal_page = new_page_instance.WebPageToWebSiteConvert()
            web_site_instance._page_dict.update(temporal_page)

        elif user_choice == '3':
            page_to_remove = input('please enter page name to remove:')
            if page_to_remove in web_site_instance._page_dict:
                del web_site_instance._page_dict[page_to_remove]
                print(f"Page '{page_to_remove}' removed successfully.")
            else:
                print(f"Page '{page_to_remove}' does not exist.")

        elif user_choice == '4':
           web_site_instance.display_info()

        elif user_choice == '5':
           new_page_name = input('Please enter new page name:')
           new_page_info = input('Please enter new page info:')

           current_datetime = datetime.now()
           current_date_formatted = current_datetime.strftime("%d-%m-%Y")

           new_temporal_page = WebPage(new_page_name,new_page_info,current_date_formatted)

           print(f'your new page is been created and is named {new_temporal_page}')
        elif user_choice == '6':
            temporal_var_page_name = input('Please enter page name:')
            if temporal_var_page_name in web_site_instance._page_dict:
                print(web_site_instance._page_dict[temporal_var_page_name])

            else: print('page not found')

        elif user_choice == '7':

            break

        else:
            print("Invalid choice. Please enter a valid option.")
