"""..."""

from dataclasses import dataclass, field

from .DataClass import DataClass


@dataclass
class BaseDrive(DataClass):
    """..."""
    drive_id: str = None
    used_size: int = None
    total_size: int = None
    drive_name: str = field(default=None, repr=False)
    owner: str = field(default=None, repr=False)
    description: str = field(default=None, repr=False)
    drive_type: str = field(default=None, repr=False)
    creator: str = field(default=None, repr=False)
    domain_id: str = field(default=None, repr=False)
    status: str = field(default=None, repr=False)
    store_id: str = field(default=None, repr=False)
    owner_type: str = field(default=None, repr=False)
    relative_path: str = field(default=None, repr=False)
    encrypt_mode: str = field(default=None, repr=False)
    encrypt_data_access: bool = field(default=None, repr=False)
    permission: str = field(default=None, repr=False)
    created_at: str = field(default=None, repr=False)
    subdomain_id: str = field(default=None, repr=False)
    category: str = field(default=None, repr=False)
