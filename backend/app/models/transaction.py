from datetime import datetime
from decimal import Decimal
from enum import Enum

from sqlalchemy import DateTime, Enum as SqlEnum, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class TransactionType(str, Enum):
    TRANSFER = "transfer"
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class TransactionStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    sender_wallet_id: Mapped[int | None] = mapped_column(ForeignKey("wallets.id"), nullable=True)
    receiver_wallet_id: Mapped[int | None] = mapped_column(ForeignKey("wallets.id"), nullable=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    type: Mapped[TransactionType] = mapped_column(
        SqlEnum(TransactionType, name="transaction_type"),
        nullable=False,
    )
    status: Mapped[TransactionStatus] = mapped_column(
        SqlEnum(TransactionStatus, name="transaction_status"),
        nullable=False,
    )
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    sender_wallet: Mapped["Wallet | None"] = relationship(
        back_populates="sent_transactions",
        foreign_keys=[sender_wallet_id],
    )
    receiver_wallet: Mapped["Wallet | None"] = relationship(
        back_populates="received_transactions",
        foreign_keys=[receiver_wallet_id],
    )
