import logging

from bot.repository.user_repository import UserRepository


class UserService:
    def __init__(self, config: dict, repo: UserRepository):
        self.repository = repo
        self.config = config

    def replace_admins(self):
        for admin in self.repository.get_admins():
            self.repository.delete_user(admin.tg_user_id)
        admin_user_ids = self.config['admin_user_ids'].split(',')
        for admin_user_id in admin_user_ids:
            logging.info(f'Add user {admin_user_id} as admin')
            self.repository.add_user(admin_user_id, 'ADMIN')

    def get_user_ids(self):
        return [user.tg_user_id for user in self.repository.list_users()]

    def add_user(self, user_id: int):
        logging.info(f'Add user {user_id} as USER')
        self.repository.add_user(user_id, 'USER')

    def remove_user(self, user_id):
        logging.info(f'Removing user {user_id}')
        self.repository.delete_user(user_id)
